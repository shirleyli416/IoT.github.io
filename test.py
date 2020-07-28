import json


dictPutall = json.load(open('json/dictAllPut.json','r'))
dictpcap = dictPutall['pcap7']
for key in dictpcap:
    print(type(dictpcap[key]))
    if dictpcap[key]:
        if dictpcap[key][0][0:3]=='GET':
            newkey= key+'2'
            print(newkey)
            if str(int(key)+2) in dictpcap and dictpcap[str(int(key)+2)]:
                if dictpcap[str(int(key)+2)][1]=="The light is off":
                    print('test')



                #
                # {% if dictPutall[key] %}
                #     {% if dictPutall[key][0][0:3]=='GET'%}
                #         {% newkey = key+2 %}
                #         {% if (str(int(key)+2)) in dictPutall and dictPutall[str(int(key)+2)]%}
                #             {% if dictPutall[str(int(key)+2)][1]=="The light is off": %}
                #                 <img class="img-responsive" src="../static/off.jpg" style="width:100%" alt="">
                #                 <P>User did not operate the app</P>
                #             {%elif dictPutall[str(int(key)+2)][1]=="The light is on" %}
                #                 <img class="img-responsive" src="../static/on.jpg" style="width:100%" alt="">
                #                 <P>User did not operate the app</P>
                #             {%else%}
                #                 <img class="img-responsive" src="../static/bright.jpg" style="width:100%" alt="">
                #                 <P>User did not operate the app</P>
                #             {%endif%}
                #         {%endif%}
                #     {%endif%}
                #     {%if dictPutall[key][0][0:3]=='PUT'%}
                #         {%if dictPutall[key+2][1]=="User Turn off the light"%}
                #             <img class="img-responsive" src="../static/off.jpg" style="width:100%" alt="">
                #             <P>User Turn off the light</P>
                #         {%elif dictPutall[key+2][1]=="User Turn on the light"%}
                #             <img class="img-responsive" src="../static/on.jpg" style="width:100%" alt="">
                #             <P>User Turn on the light</P>
                #         {%elif dictPutall[key+2][0:25]=="User Change the bright to"%}
                #             <img class="img-responsive" src="../static/bright.jpg" style="width:100%" alt="">
                #             <P>User Change the bright</P>
                #         {%else%}
                #             <img class="img-responsive" src="../static/scene.jpg" style="width:100%" alt="">
                #             <P>User Change the Bulb Scene</P>
                #         {%endif%}
                #     {%endif%}
                # {%endif%}