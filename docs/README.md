
1. Create an ssh key
2. Add the pubkey to a deploy key
3. Add the private key to a secret in the repo called `DEPLOY_KEY`
4. mkdir docs build
5. Add build to .gitignore
6. sphinx-quickstart -q -a 'Adam Frank <afrank@mozilla.com>' -v '0.0.1' --ext-autodoc --ext-coverage --ext-doctest --ext-githubpages -p cloudsecrets docs
sphinx-apidoc -f -o docs ./
7. Add the gh actions yaml to .github/workflows/
