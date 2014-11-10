%% http://darkpgmr.tistory.com/106
%% SVD population estimation

yr = [1930, 1940, 1949, 1960, 1970, 1980, 1990, 2000, 2010]';
pop = [2044, 2355, 2017, 2499, 3144, 3741, 4339, 4599, 4799]';
% pop = yr * x

A = [yr.^2 yr ones(length(yr),1)];
B = pop;
% B = A(x)

[U D V] = svd(A);

% pseudo inverse with full SVD
D_inv = D;
D_inv(1,1) = 1/D(1,1);
D_inv(2,2) = 1/D(2,2);
D_inv(3,3) = 1/D(3,3);

A_pinv = V*D_inv'*U';
X_approx = A_pinv*B;
pop_approx = A*(X_approx);
figure;
plot(yr, pop, '*', yr, pop_approx);

% pseudo inverse with truncated SVD (t=2)
D_inv = D;
D_inv(1,1) = 1/D(1,1);
D_inv(2,2) = 1/D(2,2);
D_inv(3,3) = 0;

A_pinv = V*D_inv'*U';
X = A_pinv*B;
pop_approx = A*X;
figure;
plot(yr, pop, '*', yr, pop_approx);

% pseudo inverse with truncated SVD (t=1)
D_inv = D;
D_inv(1,1) = 1/D(1,1);
D_inv(2,2) = 0;
D_inv(3,3) = 0;

A_pinv = V*D_inv'*U';
X = A_pinv*B;
pop_approx = A*X;
figure; 
plot(yr, pop, '*', yr, pop_approx);

