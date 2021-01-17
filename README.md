# Photographer portfolio
## Table of contents
* [General info](#general-info)
* [Live demo](#live-demo)
* [Features](#features)
* [Structure](#structure)
  * [Description](#description)
  * [Django apps](#django-apps)
* [Requirements](#requirements)
  * [Python packages](#python-packages)
  * [External libraries](#external-libraries)

## General info
Photographer portfolio is a website built for a friend of mine.
![](https://i.imgur.com/FgB1tpC.png)

## Live demo
Live web demo is available at [gerd.mszanowski.pl](https://gerd.mszanowski.pl).
Website is hosted on VPS (nginx, gunicorn).

### Features
- Website is fully responsive - mobile, tablet, desktop;
- Administrators can manage galleries, photos, bio section and social links through customised Django Admin,
- Visitors can send messages via form in bio section.

## Structure
### Description
This website is based on Django (both backend and frontend) and is divided into two main parts:
* **public site** where people can see galleries and images (homepage, galleries, bio)
* **admin site** where an administrator can manage the content (basically a modifed built-in Django's admin site)

**Note:** I decided to use built-in Django's admin site in view of customer's requirements.

### Django apps
- **Galleries** - displaying, adding, modifying and deleting galleries and images inside them,
- **Infos** - displaying and modifying bio section.

## Requirements

### Python packages
| **PACKAGE NAME**    | VERSION |
| ------------------- | ------- |
| django              | 3.1     |
| Pillow              | 8.0.1   |

Full `pip freeze` can be found in [requirements.txt](requirements.txt).

### External libraries

| LIBRARY NAME                              | VERSION |
| ----------------------------------------- | ------- |
| [bootstrap](https://getbootstrap.com/)    | 4.0.0   |
| [jquery](https://jquery.com/) (bootstrap) | 3.2.1   |
