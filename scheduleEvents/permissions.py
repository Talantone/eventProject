from rest_framework import permissions


class IsOwnerOrManager(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.participant_list.all())
        participants = [participant for participant in obj.participant_list.all()]
        return request.user in participants or request.user == obj.location.manager or request.user == obj.owner
