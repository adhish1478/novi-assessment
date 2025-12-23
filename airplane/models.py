from django.db import models


# Airport model represents a NODE in the tree
class Airport(models.Model):

    LEFT = "L"
    RIGHT = "R"

    POSITION_CHOICES = (
        (LEFT, "Left"),
        (RIGHT, "Right"),
    )

    # Airport code like BLR, COK, etc
    airport_code = models.CharField(
        max_length=10,
        unique=True
    )

    # duration = distance from parent airport to this airport
    # for root node this will be 0
    duration = models.PositiveIntegerField()

    # Parent airport (tree relationship)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    # Whether this airport is left or right child of parent
    position = models.CharField(
        max_length=1,
        choices=POSITION_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.airport_code

    # Helper to get left child
    @property
    def left_child(self):
        return self.children.filter(position="L").first()

    # Helper to get right child
    @property
    def right_child(self):
        return self.children.filter(position="R").first()
