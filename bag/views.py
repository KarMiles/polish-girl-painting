from django.shortcuts import render


def view_bag(request):
    """
    A view which renders the bag contents page
    """

    return render(request, 'bag/bag.html')
