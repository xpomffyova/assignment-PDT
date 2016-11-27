import flask
from flask import jsonify
from flask import Flask
from flask import render_template
import psycopg2
import json
from flask import request


app = Flask(__name__)

def connection():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    c.execute("select * from osm_point limit 10")
    rows = c.fetchall()
    for r in rows:
        print(r[0])

@app.route("/select1")
def select1():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    c.execute("select ST_AsGeoJSON(ST_Transform(way,4326)) from osm_point where name is not null limit 1000")
    rows = c.fetchall()
    for r in rows:
        print(r[0])

    resp = jsonify(rows)
    resp.status_code = 400
    return resp

# zobrazenie vsetkych
@app.route("/select2")
def select2():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand)) As properties FROM osm_point where amenity like 'fuel' and brand is not null ) As f )  As fc;")
    rows = c.fetchall()
    for row in rows:
        mystr=row
    resp = json.dumps(mystr)
#    resp.status_code = 400
    return resp

# hladanie v okoli bodu
@app.route("/select3")
def select3():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    lat = request.args.get('lat')
    lng = request.args.get('lng')
   # c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand)) As properties FROM osm_point where (amenity like 'fuel' and brand is not null) ORDER BY (ST_Distance((ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(ST_GeomFromText(ST_AsText(way) ,4326),26986)))) ) As f )  As fc;")
    c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand,(SELECT ST_Distance(ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986)))/1000)) As properties FROM osm_point where (amenity like 'fuel' and brand is not null) ORDER BY (SELECT ST_Distance(ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986))) limit 10 ) As f )  As fc;")
    rows = c.fetchall()

    for row in rows:
        mystr=row
    resp = json.dumps(mystr)
#    resp.status_code = 400
    print(resp)
    print("hhhhhhhhhhhh"+ request.args.get('lat'))
    print(request.args.get('lng'))
    s = "ahoj"
    return resp

# hladanie podla znacky
@app.route("/select4")
def select4():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    name = request.args.get('name')
    print(name)
   # c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand)) As properties FROM osm_point where (amenity like 'fuel' and brand is not null) ORDER BY (ST_Distance((ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(ST_GeomFromText(ST_AsText(way) ,4326),26986)))) ) As f )  As fc;")
    #c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand)) As properties FROM osm_point where (amenity like 'fuel' and brand is not null) ORDER BY (SELECT ST_Distance(ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986))) limit 20 ) As f )  As fc;")
    c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand)) As properties FROM osm_point where amenity like 'fuel' and UPPER(brand) like '"+name+"' ) As f )  As fc;")

    rows = c.fetchall()

    for row in rows:
        mystr=row
    resp = json.dumps(mystr)
    print(resp)

    return resp

@app.route("/select5")
def select5():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    name = request.args.get('name')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    print(name)
    c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand,(SELECT ST_Distance(ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986)))/1000)) As properties FROM osm_point where amenity like 'fuel' and UPPER(brand) like '"+name+"' Order by (SELECT ST_Distance(ST_Transform(ST_GeomFromText ('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986))) limit 10) As f )  As fc;")

    rows = c.fetchall()

    for row in rows:
        mystr=row
    resp = json.dumps(mystr)
    print(resp)

    return resp


@app.route("/select6")
def select6():
    try:
        con = psycopg2.connect(dbname='osm', host='localhost', port=5432, user='postgres', password='hesielko')
    except:
        print("error")
    c = con.cursor()
    dist = request.args.get('dist')

    lat = request.args.get('lat')
    lng = request.args.get('lng')
    print(dist)
    c.execute("SELECT row_to_json(fc) FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type , ST_AsGeoJSON(ST_Transform(way,4326))::json As geometry, row_to_json((osm_id,brand,(SELECT ST_Distance(ST_Transform(ST_GeomFromText('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986)))/1000)) As properties FROM osm_point where amenity like 'fuel' and brand is not null and ((SELECT ST_Distance(ST_Transform(ST_GeomFromText ('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986))) < "+ dist+") order by (SELECT ST_Distance(ST_Transform(ST_GeomFromText ('POINT(" + lng + " " + lat + ")',4326),26986),ST_Transform(way,26986))) limit 30 ) As f )  As fc;")
    rows = c.fetchall()
    for row in rows:
        mystr=row
    resp = json.dumps(mystr)
    print(resp)

    return resp


@app.route("/")
def hello():
    print("halooo")
    connection()
    return render_template("index.html")

def main():
   print("meth1")

if __name__ == "__main__":
    print("meth1")
    app.run()






