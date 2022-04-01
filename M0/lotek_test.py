from lotek import random_generator


def test_random_generator():
    #given
    #when
    items = random_generator()
    res=[]
    for _ in range(501):
        for i in items:
            if i not in res:
                if i>0 and i<50:
                    res.append(i)

        #random_generator = sorted(list(random_generator()))

    # #then
    assert len(items)==6
    assert len(res)==6
    #assert random_generator[0]>=1
    #assert random_generator[-1]<50