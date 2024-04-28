import ragbear

bear = ragbear.from_config("config.yaml")
ans = bear.query("Where was Steve Jobs born?", strategy="replug")
print(ans)
