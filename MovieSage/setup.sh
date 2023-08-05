mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"akankshamahankar1112@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
