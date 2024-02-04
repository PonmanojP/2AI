# signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ML,DL,Vision,Bigdata,NLP,Edge,Cloud,Web,Design,DeletedItem


@receiver(pre_delete, sender=ML)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=DL)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Vision)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Bigdata)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=NLP)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Edge)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Cloud)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Web)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )

@receiver(pre_delete, sender=Design)
def save_deleted_item(sender, instance, **kwargs):
    deleted_item = DeletedItem.objects.create(
        Announcement1=instance.Announcement1,
        Announcement2 = instance.Announcement2,
        Announcement3 = instance.Announcement3,
        Link_text_1 = instance.Link_text_1,
        Link_text_2 = instance.Link_text_2,
        Link_text_3 = instance.Link_text_3,
        Link_text_4 = instance.Link_text_4,
        Link_1 = instance.Link_1,
        Link_2 = instance.Link_2,
        Link_3 = instance.Link_3,
        Link_4 = instance.Link_4,
        # Add other fields as needed
    )
