# Shortify

A URL shortener takes some long, unwieldy link and turns it into a shorter link, one that's easy to share.

- For example:
  - Input: https://youtu.be/Li0Abz-KT78
  - Output: https://shrtco.de/qTsuEz
   
  
## Table of Contents

- [Introduction](#Introduction)  
- [Getting Started](#Getting-Started)  
- [Tech Stack](#Tech-Stack)
- [Installation](#Installation)
    

## Introduction

While **Shortify** used to be useful for shortening longer links to fit character limits on social media and messaging apps, a lot of platforms take care of that for you. **Shortify** allow you to provide a typable link on a business card, print ad, podcast interview, or any other situation where someone can't just click on a nice hyperlink. 

## Getting Started

Clone or download this repository.
> $ git clone https://github.com/sajiya21/polynomial_assignment.git 

> $ python ./main.py

## Tech Stack

A simple web application built with

- Flask  
- MongoDB
- Requests
- CryptoCode
- Socket

## Installation

You can install above packages using following command:
> $ pip install Flask, pymongo, dnspython, requests, cryptocode

Or you can install from source with:
> $ pip install requirements.txt

## Project Structure
```
|   main.py
|   Procfile
|   README.md
|   requirements.txt
+---static
|   +---css
|   |       main_table.css
|   |       style.css
|   +---fonts
|   |       font-awesome-4.7.0
|   |       OpenSans         
+---templates
|       index.html
|       track.html
|       video.html
+---Utils
|       database.py
|       security.py
```