a=[3 -1 -2;1 -4 1;-2 1 -3];

n=size(a,1);    

c1=0;

c2=0;

for i=1:n

    s(i)=0;

    for j=1:n

        if i~=j   

            s(i)=s(i)+abs(a(i,j));

        end

    end

    if abs(a(i,i))>s(i)

        c1=c1+1;

    end

    if abs(a(i,i))>=s(i)

        c2=c2+1;

    end

end

c1

c2