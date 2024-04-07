def util_for_sessions(session_key, request, post):
    if session_key:
        if 'viewed_posts' not in request.session:
            request.session['viewed_posts'] = []
        post_id = post.id
        if post_id not in request.session['viewed_posts']:
            request.session['viewed_posts'].append(post_id)
            post.increment_views()