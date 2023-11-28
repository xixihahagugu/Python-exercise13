def prinum(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return ture
        else:
            return False



from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<num>')
def x(num):
    number=int(num)
    response = {
        "Number" : number,
        "isPrime":prinum(number)
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)