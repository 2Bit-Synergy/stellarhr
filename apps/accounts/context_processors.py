def user_role(request):
    group_names = request.user.groups.values_list('name', flat=True)
 
    return {'user_role': group_names[0] if group_names else None}