from django import template


register = template.Library()

CENSOR_WORDS = {'kek','shrek','lel' }

@register.filter()
def censor(value):
    k = 0
    new_list_words = []
    list_words = value.split()
    for word in list_words:
        if word not in CENSOR_WORDS:
            new_list_words.append(word)
        if word in CENSOR_WORDS:
            length = len(word)
            if length <= 2:
                new_list_words.append(word[0] + (length-1)*'*')
            else:
                new_list_words.append(word[0] + (length-2)*'*' + word[-1])
    return(' '.join(new_list_words))
