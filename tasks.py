from invoke import task

@task
def build_docker_image(c):
    c.run("poetry export --dev --without-hashes -f requirements.txt > requirements.txt")
    c.run(f"DOCKER_BUILDKIT=1 docker build -t producer-consumer -f Dockerfile .")
    c.run("rm -f requirements.txt")


@task(build_docker_image)
def run(c, detached=False):
    if detached:
        c.run("docker compose up -d")
    else:
        c.run("docker compose up")

@task
def manage(c, cmd):
    """
    Commands to Django manage.py (https://docs.djangoproject.com/en/3.2/ref/django-admin/)
    """
    c.run(f"docker-compose exec api python manage.py {cmd}")