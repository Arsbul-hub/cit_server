from app import application, game_api_routes, login_api_routes, db_session, db

if __name__ == '__main__':
    with application.app_context():
        # db.drop_all()
        db.create_all()
        db.session.commit()
    # db_session.global_init("app.db")


    application.run(host='0.0.0.0', port=5000, debug=False)
