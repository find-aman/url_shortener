## url_shortener
**WeeIt** - URL Shortener application built using Django

**Try Out The App :** [https://weeit.herokuapp.com/](https://weeit.herokuapp.com/)

**Features of the application:-**
- Able to short URL up to 200 characters long.
- Able to give custom unique shortcodes to the URLs.

**Steps to run the application:-**
*Assumption python 3  is installed properly*
1. Clone this repository.
2. Open the folder created and open cmd in it.
3. Install virtual environment by `pip install virtualenv`
4. Create a virtual environment by `virtualenv venv` 
5. Activate the virtual environment by `venv\Scripts\activate`
6. Install all the packages from requirments.txt file by `pip install -r requirements.txt`
7. Now create some User Environment Variables with names like.
	- **DEBUG_VALUE**(set value True for testing)
	- **SECRET_KEY**(set value to a newly generated secret key using *secrets* module in python using `token_hex(24)`)
8. Change the value of **WEEIT_URL** to http://localhost:8000/ in *setting.py* file
9. Make migrations by `python manage.py migrate`
10. Create a superuser to admin testing by `python manage.py createsuperuser` and enter the details asked.
11. Then run the server by `python manage.py runserver` 

**Testing of Features:-**
- Enter the long URL. Click on **Short URL** button, you will get the shortened URL.
- Click on **New** and enter any long URL again.
- Check on the **Custom Shortcode** checkbox and enter a uniques custom shortcode and click **Short URL**.
- You will get a short URL with your custom shortcode.
