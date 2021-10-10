registerAluOverride(0,
function(inputs,outputs)
{
var volta = 0;
for (var n=0;n<components.length;n++)
{
var c = components[n];
if (c.value)
{
volta = Math.round(Math.sqrt(n))+volta;
}
}
for (var n=0;n<outputs.length;n++)
{
outputs[n] = (volta >> n)%2;
}
});