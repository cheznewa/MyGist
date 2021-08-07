// Le PT, Une Unité De Mesure BLE TOU; 1 Mettre = 4.61 PT
registerAluOverride(0,
function(inputs,outputs)
{
var pos = 0;
for (var n=0;n<inputs.length;n++)
{
pos += inputs[n] << n;
}
if (pos == 0)
{
var fn = 4
}
else
{
pos = pos+1;
var u = pos*pos;
var uu = u.toString();
var ll = uu.length;
var ss = 0;
for (var n=0;n<ll;n++)
{
ss += parseInt(uu[n]);
}
var fn = 10 - (ss % 10);
if (fn == 10)
{
fn = 0;
}
}
for (var n=0;n<4;n++)
{
outputs[n] = (fn >> n)%2;
}
});