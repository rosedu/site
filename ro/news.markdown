---
layout: basero
---

{% for post in site.categories.ro %}
<div class="post-container">
	<div class="entry-title">
		<h2><a href="{{post.url}}">{{ post.title }}</a></h2>
	</div>
	<div class="entry-meta">
		Publicat de {{post.author}} la {{post.date | date: '%d %B %Y'}}
	</div>
	<div class="entry-content">
		{{ post.content }}
	</div>
</div>
{% endfor %}
