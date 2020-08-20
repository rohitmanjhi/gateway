# gateway

1. First install python3 or pip3 in our system

2. then, pip3 install pipenv (its help to create virtual environment)

3. then, Go to retail directry and install requirements.txt
    pipenv install -r requirements.txt

4. then, python manage.py makemigrations

5. python manage.py migrate

6. python manange.py runserver

7. Check test cases,
   python manage.py test

8. url - http://127.0.0.1:8000/app/get_or_post_payment_gateway
   payload request data =>
   {
    "amount":"180.23",
    "currency": "INR",
    "type": "debitcard",
	  "card": {
		"number": "4111111111111111",
		"expirationMonth": "2",
		"expirationYear": "2020",
		"cvv": "111"
  	}
  } 
