import orcid, math

###  API will only return 100 results at a time.

### Declare some stuff

api = orcid.PublicAPI(institution_key="YOURKEYHERE", institution_secret="YOURSECRETHERE")
ror = "YOUR ROR HERE: ex: https://ror.org/03jep7677"


def get_orcids(ror):
    my_orcids = []
    results = api.search(('ror-org-id:"{}"'.format(ror)))
    num_records = results['num-found']
    call_num = math.ceil(num_records/100)
    run = 1

    while run <= call_num:
        if run == 1:
            results = api.search(('ror-org-id:"{}"'.format(ror)))
            for i in results['result']:
                #print(i['orcid-identifier']['uri'])
                my_orcids.append(i['orcid-identifier']['path'])
            run +=1
        else:
            rec_start = ((run*100)-100)
            results = api.search(('ror-org-id:"{}"'.format(ror)), start=rec_start)
            for i in results['result']:
                # print(i['orcid-identifier']['uri'])
                if i not in my_orcids:
                    my_orcids.append(i['orcid-identifier']['path'])
            run +=1
    return(my_orcids)

test = get_orcids(ror)
print(len(test))
