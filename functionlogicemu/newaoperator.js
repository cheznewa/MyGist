registerAluOverride(0,
function(inputs,outputs)
{
var r = 0;
for (var h=0;h<inputs.length;h++)
{
outputs[h] = (inputs[h*2] | inputs[(h*2)+1]) ^ r;
r = inputs[h*2] & inputs[(h*2)+1];
}
});