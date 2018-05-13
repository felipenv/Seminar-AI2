function [distance] = A_heuristics(possibleNextNode, targetNode, paths_bots,stepNumber)
%check for forbidden nodes
for i=1:length(paths_bots)
    %check if possibleNextNode is forbidden node
    if (stepNumber<length(paths_bots{i})-1)
        if possibleNextNode==paths_bots{i}(stepNumber)
            distance=inf;
            return
        end
        %check if possibleNextNode is forbidden node because overlaps with 1
        %step ahead
        if possibleNextNode==paths_bots{i}(stepNumber+1)
            distance=inf;
            return
        end
%         if possibleNextNode==paths_bots{i}(stepNumber+2)
%             distance=inf;
%             return
%         end    
        if stepNumber>2
            if possibleNextNode==paths_bots{i}(stepNumber-2)
                 distance=inf;
                 return
            end
        end
        if possibleNextNode==paths_bots{i}(stepNumber-1)
            distance=inf;
            return
        end
    end

end

%if it's not forbidden check manhattan distance
distance=abs(mod(possibleNextNode-1,5)-mod(targetNode-1,5));
distance=distance+abs(floor((possibleNextNode-1)/5)-floor((targetNode-1)/5));

end