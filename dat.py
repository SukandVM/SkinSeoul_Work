import pandas as pd
from huggingface_hub import login
import re
from flask import Flask, request, jsonify, render_template
from agent_runner import run_agent_prompt
import datetime

login(token="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")
app = Flask(__name__)
data = pd.read_csv('Mock_Skincare_Dataset - Data.csv')

manual_overrides = set()
def compute_scores(df):
    df = df.copy()
    df["score"] = df["Views Last Month"] * 0.3 + df["Volume Sold Last Month"] * 1.5
    return df

def get_ranked_products(top_n=5):
    
    df = compute_scores(data)

    
    override_df = df[df["Product Name"].isin(manual_overrides)].copy()
    override_df["score"] = 9999  

   
    remaining_df = df[~df["Product Name"].isin(manual_overrides)].copy()
    remaining_df = remaining_df.sort_values(by="score", ascending=False)


    combined_df = pd.concat([override_df, remaining_df])
    combined_df = combined_df.drop_duplicates(subset="Product Name", keep="first")

    
    return combined_df.head(top_n).to_dict(orient="records")

import re

def is_valid_result_code(code):
    """
    Validates that the code is a single Python line assigning a list to `result`.
    e.g., result = ['a', 'b', 'c']
    """
    pattern = r"^\s*result\s*=\s*\[.*?\]\s*$"
    return re.match(pattern, code.strip()) is not None

#Page Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommendations", methods=["GET"])
def recommendations():
    top_n = int(request.args.get("top_n", 5))
    return jsonify(get_ranked_products(top_n))

@app.route("/ai-recommendations", methods=["POST"])
def ai_recommend():
    data = pd.read_csv('Mock_Skincare_Dataset - Data.csv')
    prompt = request.json.get("prompt")
    code = None  
    try:
        
        code = run_agent_prompt(prompt,data)
        print("📥 Prompt:", prompt)
        print("🧠 Generated Code:\n", code)

        
        local_scope = {
            'df': data.copy() 
        }

        
        exec(code, {}, local_scope)

        
        result = local_scope.get("result", None)

        
        if not isinstance(result, list):
            raise ValueError("Code executed and a valid list was produced in `result`.")

        print("✅ Final AI Result:", result)
        return jsonify(result)

    except Exception as e:
        print("Local Scope:", local_scope.keys())
        print("Faulty code:\n",code)
        print("❌ Error in AI route:", str(e))
        return jsonify({
            "error": str(e),
            "code": code if code else "No code generated"
        }), 500

    
@app.route("/override", methods=["POST"])
def override_add():
    payload = request.get_json()
    name = payload.get("product_name")
    if name and name in data["Product Name"].values:
        manual_overrides.add(name)
        with open("logs/overrides.log", "a") as f:
            f.write(f"{datetime.datetime.now().isoformat()} - OVERRIDE: {name}\n")

        return jsonify({"status": "override added", "product_name": name})
    return jsonify({"status": "error", "message": "Invalid product name"}), 400

@app.route("/overrides", methods=["GET"])
def list_overrides():
    return jsonify(list(manual_overrides))

@app.route("/reset", methods=["POST"])
def reset_overrides():
    manual_overrides.clear()
    return jsonify({"status" : "overrides cleared"})

if __name__ == "__main__":
    app.run(debug=True)



