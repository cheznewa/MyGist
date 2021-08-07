registerAluOverride(0,
function(inputs,outputs)
{
var pos = 0;
for (var n=0;n<inputs.length;n++)
{
pos += inputs[n] << n;
}
var http = new XMLHttpRequest();
http.open("GET","https://api.pi.delivery/v1/pi?start="+pos+"&numberOfDigits=1",false);
http.send();
const j = http.responseText;
const jo = JSON.parse(j);
for (var n=0;n<4;n++)
{
outputs[n] = (parseInt(jo.content) >> n)%2;
}
});