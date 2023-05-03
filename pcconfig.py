import pynecone as pc

config = pc.Config(
    app_name="pyne",
    api_url = 'http://i02prf9.p.ssafy.io:8000',
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        "react-colorful",
    ]
)

