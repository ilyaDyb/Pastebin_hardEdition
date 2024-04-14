from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.db.models import Q

from posts.models import Post


def util_for_sessions(session_key, request, post):
    if session_key:
        if 'viewed_posts' not in request.session:
            request.session['viewed_posts'] = []
        post_id = post.id
        if post_id not in request.session['viewed_posts']:
            request.session['viewed_posts'].append(post_id)
            post.increment_views()



def q_search(query):
    vector = SearchVector("title")
    search_query = SearchQuery(query)
    exact_match = Post.objects.filter(title__exact=query).first()

    if exact_match:
        result = Post.objects.filter(pk=exact_match.pk)
    else:
        result = (Post.objects.annotate(rank=SearchRank(vector=vector, query=search_query))
                  .filter(rank__gt=0).order_by("-rank"))

    result = result.annotate(
        headline=SearchHeadline(
            "title",
            search_query,
            start_sel='<b class="card-title" style="background-color: yellow;">',
            stop_sel="</b>",
        )
    )

    return result