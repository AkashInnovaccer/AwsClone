from flask import Flask,render_template,url_for,request,redirect
import s3
import ec2
import boto3

app = Flask(__name__)
  

# session = boto3.Session(
#     aws_access_key_id="AKIAWGZBXL66E7FVKL67" ,
#     aws_secret_access_key="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" ,
# )


@app.route('/')
def root():
    return render_template("index.html")
#s3

@app.route('/s3/list')
def s3list():
    li=s3.listbuckets()
    return render_template("s3list.html",li=li)


@app.route('/s3/create')
def s3create():
    return render_template("s3create.html")

@app.route('/s3/created',methods=["POST"])
def s3created():
    if request.method == "POST":
        name = request.form["cname"]
        print(name)
        s3.createbucket(name)
        return redirect(url_for("s3list"))

@app.route('/s3/delete')
def s3delete():
    return render_template("s3delete.html")

@app.route('/s3/deleted',methods=["POST"])
def s3deleted():
    if request.method == "POST":
        name = request.form["cname"]
        print(name)
        s3.deletebuckets(name)
        return redirect(url_for("s3list"))
#ec2
@app.route('/ec2/list')
def ec2list():
    li=ec2.get_running_instances()
    return render_template("ec2list.html",li=li)


@app.route('/ec2/public')
def ec2public():
    li=ec2.get_public_ip()
    return render_template("ec2public.html",li=li)

@app.route('/ec2/create')
def ec2create():
    ec2.create_instance()
    return render_template("index.html")


# @app.route('/ec2/created')
# def ec2created():
#     ec2.create_instance()


@app.route('/ec2/stop')
def ec2stop():
    return render_template("ec2stop.html")

@app.route('/ec2/stopped',methods=["POST"])
def ec2stopped():
    if request.method == "POST":
        id=request.form["id"]
        ec2.stop_instance(id)
        return redirect(url_for("ec2list"))


@app.route('/ec2/terminate')
def ec2terminate():
    return render_template("ec2terminate.html")


@app.route('/ec2/terminated',methods=["POST"])
def ec2terminated():
    if request.method == "POST":
        id=request.form["id"]
        ec2.terminate_instance(id)
        return redirect(url_for("ec2list"))

if __name__ == '__main__':
   app.run(debug=True,host="0.0.0.0")

