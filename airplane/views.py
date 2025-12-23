from django.shortcuts import render, redirect
from .forms import AirportForm, NthNodeForm, BetweenAirportForm
from .models import Airport

# This view is used to ADD airports (nodes) into the tree
# One airport = one node in the binary tree
def add_airport(request):

    # If user submits the form
    if request.method == 'POST':
        form = AirportForm(request.POST)

        # Validate form data
        if form.is_valid():
            # Save airport into DB
            form.save()

            # Redirect to same page so user can add more nodes
            return redirect('add_airport')

    # If request is GET, just show empty form
    else:
        form = AirportForm()

    # tree is passed so we can show current tree on left side
    return render(
        request,
        'airplane/add_airport.html',
        {
            'form': form,
            'tree': get_airport_tree()
        }
    )


# Helper function for Question 1
# From a starting node, move left/right N times
def find_nth(start_node, direction, n):
    current = start_node

    # Move step by step N times
    for _ in range(n):
        try:
            # children.get(position=direction) gives left or right child
            current = current.children.get(position=direction)
        except Airport.DoesNotExist:
            # If path breaks before N steps
            return None

    return current


# View for Question 1:
# Find Nth Left or Right node
def nth_node_view(request):
    result = None

    if request.method == 'POST':
        form = NthNodeForm(request.POST)

        if form.is_valid():
            start_airport = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']
            n = form.cleaned_data['n']

            # Call helper function
            result = find_nth(start_airport, direction, n)
    else:
        form = NthNodeForm()

    return render(
        request,
        'airplane/nth_node.html',
        {
            'form': form,
            'result': result,
            'tree': get_airport_tree()
        }
    )


# Question 2:
# Longest route = max distance between parent and child
def longest_node_view(request):

    # duration is stored on child node (edge weight)
    node = Airport.objects.order_by('-duration').first()

    return render(
        request,
        'airplane/longest_node.html',
        {
            'node': node,
            'tree': get_airport_tree()
        }
    )


# Helper function:
# Get path from a node to root (used in Question 3)
def path_to_root(node):
    path = []

    # Go up till root
    while node:
        path.append(node)
        node = node.parent

    return path


# Core logic for Question 3
# Find shortest DISTANCE (edge) between two airports
def shortest_between(a, b):

    path_a = path_to_root(a)
    path_b = path_to_root(b)

    # Find common nodes (to get LCA)
    common = set(path_a) & set(path_b)

    # Build full path from a to b
    full_path = []

    for n in path_a:
        full_path.append(n)
        if n in common:
            break

    for n in reversed(path_b):
        if n not in full_path:
            full_path.append(n)

    # IMPORTANT:
    # duration represents distance from parent -> child
    # so root has no meaning, we ignore it
    edge_nodes = [
        n for n in full_path
        if n.parent is not None
    ]

    # Return the node which represents shortest edge
    return min(edge_nodes, key=lambda x: x.duration)


# View for Question 3
def shortest_between_view(request):
    result = None

    if request.method == "POST":
        form = BetweenAirportForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['airport_a']
            b = form.cleaned_data['airport_b']

            result = shortest_between(a, b)
    else:
        form = BetweenAirportForm()

    return render(
        request,
        'airplane/shortest_between.html',
        {
            'form': form,
            'result': result,
            'tree': get_airport_tree()
        }
    )


# Utility function
# Root nodes are those with no parent
def get_airport_tree():
    return Airport.objects.filter(parent__isnull=True)
