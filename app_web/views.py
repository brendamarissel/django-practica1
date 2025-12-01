from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Persona
from .forms import PersonaForm

# CREATE + READ con búsqueda y paginación
def index(request):
    query = request.GET.get("buscar", "")  # texto que el usuario escribe

    personas_list = Persona.objects.filter(
        Q(nombre__icontains=query)  # icontains → no distingue mayúsculas
    )

    paginator = Paginator(personas_list, 5)  # 🔥 5 registros por página
    page = request.GET.get('page')
    personas = paginator.get_page(page)

    form = PersonaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "index.html",
                  {"form": form, "personas": personas, "buscar": query})


# UPDATE
def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    form = PersonaForm(request.POST or None, instance=persona)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "editar.html", {"form": form, "persona": persona})


# DELETE
def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.delete()
    return redirect("/")

