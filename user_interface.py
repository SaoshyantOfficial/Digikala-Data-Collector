from flask import Flask, render_template, request
import digikala

app = Flask(__name__)

# Route for the form page
@app.route('/')
def index():
    return render_template('input_page.html')

# Route for handling the form submission
@app.route('/submit', methods=['POST'])
def submit():
     
    # Get the URLs from the form
    urls = []
    for key, value in request.form.items():
        if key.startswith('url'):
            urls.append(value)

    # Print the URLs
    print(urls)
   


    for i in urls:
         instance = digikala.data_collector(i) 
     
    # Redirect to a success page or render a template with the URLs
    return render_template('result_page.html', urls=urls)

if __name__ == '__main__':
    app.run()
