def on_env(env, config, files):
    env.tests["startswith"] = str.startswith
