  gives broad capabilities, and plain `eval` allows
  `__import__('os').popen(...)` RCE; master's extra `--unsafe-policy`
  whitelist sandbox is observe-only by default).
