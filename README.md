# git-certificate

Apply what you've learned by submitting a pull-request to *git* your participation certificate by email. Your Name & Email will be encrypted so only me can view them.

Inspired by [Fireship](https://github.com/fireship-io/git-sticker)

## Instructions
> [!IMPORTANT]
> If you want to clone it locally, make sure to have python3 installed & `pip`. Otherwise you can use Github Codespaces

1. Fork this repo
2. Either open your fork with Github Codespaces OR `git clone` your fork url
3. Enter the project and run `pip install cryptography`
4. Create a new branch with `git checkout -b certs/<your-github-username>`
5. Run `python3 main.py` and follow the instructions to encrypt your address
6. Create a new file named **certs/<your-github-username>.txt** and paste in the encrypted string
7. Run `git add .` and `git commit -m "your-message"`
8. `git push origin certs/<your-github-username>`
9. Open a new PR on Github

> [!NOTE]
> Your commit must contain only 1 file. Verify that you did not change any existing code
> before making your PR. Do not commit any automatically anything else