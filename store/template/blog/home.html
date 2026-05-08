{% extends 'blog/base.html' %}

{% block title %}Explora nuestras historias | {% endblock %}

{% block content %}
<div class="container py-5">
    <header class="mb-5 text-center">
        <h1 class="display-4 fw-bold">Últimas Publicaciones</h1>
        <p class="lead text-muted">Descubre noticias, tutoriales y reflexiones de nuestra comunidad.</p>
    </header>

    <div class="row g-4 justify-content-center">
        {% for post in posts %}
        <div class="col-12 col-md-10 col-lg-8">
            <article class="card h-100 border-0 shadow-sm hover-shadow transition-all">
                <div class="row g-0 align-items-center">

                    {% if post.image %}
                    <div class="col-md-4">
                        <img src="{{post.image.url}}"
                             class="img-fluid rounded-start h-100 object-fit-cover"
                             alt="{{post.title}}"
                             >
                    </div>
                    {% endif %}

                    <div class="{% if post.image %}col-md-8{% else %}col-12{% endif %}">
                        <div class="card-body p-4">
                            <div class="mb-2">
                                <span class="badge rounded-pill text-bg-primary bg-opacity-10 text-primary">
                                    {{ post.created_at|timesince }}
                                </span>
                            </div>

                            <h2 class="card-title h3 mb-3">
                                <a href="{% url 'post_detail' post.id %}" class="text-decoration-none text-dark link-primary">
                                    {{ post.title }}
                                </a>
                            </h2>

                            <p class="card-text text-secondary mb-4">
                                {{ post.intro|truncatechars:160 }}
                            </p>

                            <div class="d-flex justify-content-between align-items-center">
                                <a href="{% url 'post_detail' post.id %}" class="btn btn-link p-0 text-decoration-none fw-bold">
                                    Leer más
                                    <i class="bi bi-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </article>
        </div>
        {% empty %}
        <div class="col-12 text-center py-5">
            <p class="lead">No hay publicaciones por ahora. ¡Vuelve pronto!</p>
        </div>
        {% endfor %}
    </div>
</div>

<style>
    .hover-shadow {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hover-shadow:hover {
        transform: translateY(-5px);
        box-shadow: 0 1rem 3rem rgba(0,0,0,.1) !important;
    }
    .object-fit-cover {
        object-fit: cover;
    }
    .transition-all {
        transition: all 0.3s ease-in-out;
    }
</style>
{% endblock %}