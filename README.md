# Cockpit CMS API

![PyPI - Version](https://img.shields.io/pypi/v/cockpit-api)
![PyPI - Downloads](https://img.shields.io/pypi/dd/cockpit-api)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/cockpit-api)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/cockpit-api)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/cockpit-api)
![PyPI - License](https://img.shields.io/pypi/l/cockpit-api)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/cockpit-api)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/cockpit-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/cockpit-api)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/cockpit-api)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/cockpit-api)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/cockpit-api)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/cockpit-api)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/cockpit-api)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/cockpit-api)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/cockpit-api)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/cockpit-api)

*Version: 0.2.0*

Cockpit CMS API Python Wrapper

Includes standard Cockpit API Calls

### API Calls:
- Get Content
- Add/Update Content
- Get Asset
- Get Image Asset

This repository is actively maintained and will continue adding more API calls

Contribution Opportunities:
- Support new API calls

<details>
  <summary><b>Usage:</b></summary>

```python
#!/usr/bin/python
# coding: utf-8
import cockpit_api

token = "<TOKEN>"
api_url = "<COCKPIT API URL>"
client = cockpit_api.Api(url=api_url, token=token)

content = client.get_content(model="<COLLECTION/SINGLETON>")
print(content)
```

</details>

<details>
  <summary><b>Installation Instructions:</b></summary>

```bash
python -m pip install cockpit-api
```

</details>

<details>
  <summary><b>Repository Owners:</b></summary>


<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
</details>
