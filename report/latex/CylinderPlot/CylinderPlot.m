cylinders = [1,-1;2,1;3,-1;4,1;5,-1;6,1];

hold on;

%nest
plot(0,0,'xk')

%fodder
plot(0,8,'sk')


for i=(1:6)
    plot(cylinders(i,2),cylinders(i,1),'.k')
end


xlim([-5,5])
ylim([-1,9])

legend('nest', 'feeding station', 'cylinder')