(define (factorial x)
  (if (< x 2) 1 (* x (factorial (- x 1)))))

(define (fib n)
  (cond
    ((<= n 0) 0)
    ((= n 1) 1)
    (else (+ (fib (- n 1)) (fib (- n 2))))))

(define (my-append a b)
  (if (null? a)
      b
      (cons (car a) (my-append (cdr a) b))))

(define (duplicate lst)
  (if (null? lst)
      nil
      (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))

(define (insert element lst index)
  (if (or (< index 0) (and (null? lst) (> index 0)))
      lst
      (if (= index 0)
          (cons element lst)
          (cons (car lst) (insert element (cdr lst) (- index 1))))))
