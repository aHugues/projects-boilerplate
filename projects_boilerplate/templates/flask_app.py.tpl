from $project_sources_dir import create_app

if __name__ == '__main__':
    app = create_app(debug=True)
    app.run(port=5000, host='0.0.0.0')
