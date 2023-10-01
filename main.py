from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>Свидетельство о браке</title>
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            background: linear-gradient(45deg, #3498db, #e74c3c, #f39c12, #1abc9c, #3498db);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .certificate {
            text-align: center;
            background-color: #ffffff; /* White certificate background */
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
            max-width: 60%;
            margin: 50px auto;
            position: relative;
            overflow: hidden;
        }

        .title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #3498db; /* Blue title color */
            position: relative;
            z-index: 1;
        }

        .details {
            font-size: 18px;
            margin-bottom: 30px;
            text-align: left;
            color: #555555; /* Dark gray text color */
            position: relative;
            z-index: 1;
        }

        .details div {
            margin-bottom: 10px;
            text-align: center;
        }

        .details div span {
            font-weight: bold;
        }

        .powered {
            font-size: 12px;
            color: #888888;
            margin-top: 20px;
            position: relative;
            z-index: 1;
        }

        .certificate::before {
            content: '';
            display: block;
            height: 10px;
            background-color: #3498db; /* Blue line color */
            border-radius: 5px;
            margin: 0 auto 20px;
            max-width: 100px;
            position: relative;
            z-index: 1;
        }

        .animated-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.6); /* Light gray background for animation */
            z-index: 0;
        }
    </style>
</head>

<body>
    <div class="certificate">
        <div class="title">Свидетельство о браке</div>
        <div class="details">
            <div><span>Дата создания:</span> {{ date }}</div>
            <div>{{ person1 }} + {{ person2 }}</div>
        </div>
        <div class="powered">Powered by City Evolution</div>
        <div class="animated-background"></div>
    </div>
</body>

</html>

"""

@app.route('/generate_certificate')
def generate_certificate():
    date = request.args.get('date')
    person1 = request.args.get('person1')
    person2 = request.args.get('person2')
    html = render_template_string(template, date=date, person1=person1, person2=person2)
    return html

if __name__ == '__main__':
    app.run(host='195.49.210.163', port=8000)
    app.run()