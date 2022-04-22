from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import  Count
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post

def blog(request):

	posts = Post.objects.all()
	paginator = Paginator(posts,6)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request,'blog/blog.html',{'page':page,'posts':posts})


def post_details(request,slug):

	post = get_object_or_404(
		Post,
		slug=slug
	)

	post_tags_ids = post.tags.values_list('id',flat=True)
	similar_posts =  Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]
	recent_posts = Post.objects.all().order_by('-publish')

	return render(request,'blog/post_details.html',{'post':post,'similar_posts':similar_posts,})