# SkinSeoul_Work

An AI Agent that recommends skin care products based on popularity</br>
Popularity is calculated using a weighted function that factors in the "Views Per Last Month" column and "Sales"</br>

The popularity function is static. In order to account for dynamic requirements, the SmolAgents framework designed by HuggingFaces was used.</br>
Manual overrides are necessary in cases where manufacturers want to promote a new product. The override push the product to the top of the list automatically.
