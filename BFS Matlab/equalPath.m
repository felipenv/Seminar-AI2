%check if all nodes were visited except the target node 
function [equal] = equalPath(paths,newPath)
equal=false;
for i=1:length(paths)
    paths{i};
    newPath;
    if isequal(paths{i},newPath)
       equal=true;
    end
    
end

end