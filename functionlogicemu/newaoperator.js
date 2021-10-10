var a = 8;
registerAluOverride(0,
function(inputs,outputs)
{
var r = 0;
for (var h=0;h<a;h++)
{
outputs[h] = (inputs[h] | inputs[h+a]) ^ r;
r = inputs[h] & inputs[h+a];
}
});