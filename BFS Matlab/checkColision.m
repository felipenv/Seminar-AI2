function [colide,i] = checkColision(path1, path2)
    
    colide=false;
    len1=length(path1);
    len2=length(path2);
    len=min(len1,len2);
    for i=1:len
        if len1>len2
            if path1(i)==path2(i) || path1(i+1)==path2(i)
                colide=true;
                return
            end
        else
            if path1(i)==path2(i) || path1(i)==path2(i+1)
                colide=true;
                return
            end
        end
    end
end