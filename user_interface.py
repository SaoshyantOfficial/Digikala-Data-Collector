import logging
from flask import Flask, render_template, request
import digikala

app = Flask(__name__)

class InvalidInputError(Exception):
    pass

@app.route('/')
def index():
    """
    Render the input page.
    """
    return render_template('input_page.html')


@app.route('/submit', methods=['POST'])
def submit():
    """
    Handle the form submission.
    """

    try:
        # Get the review URLs from the form
        review_urls = []
        for key, value in request.form.items():
            if key.startswith('url'):
                if not value.startswith('https://www.digikala.com/product/'):
                    raise InvalidInputError("Invalid review URL: {}".format(value))
                review_urls.append(value)

        # Scrape reviews from the review URLs
        instance = digikala.Digikala(review_urls)
        instance.collector()

        # Check if any error has been occurred
        if instance.error:
            return render_template("errorPage.html", message = "خطایی رخ داد، لطفا فایل لاگ را بررسی کنید")
        
        else: # Render result page if every thing isok
            return render_template('result_page.html')
            
    except InvalidInputError as e:
        # Return a 400 Bad Request response if the input was invalid
        logging.error(str(e))
        return ('Invalid input: {}'.format(str(e)), 400)

    except Exception as e:
        # Log any other errors and return a 500 Internal Server Error response
        logging.exception("Error handling form submission: %s", e)
        return ('Internal server error', 500)


if __name__ == '__main__':
    app.run(debug=True)