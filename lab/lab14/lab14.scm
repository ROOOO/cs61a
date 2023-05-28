(define (split-at lst n)
  'YOUR-CODE-HERE
  (define (helper lst-so-far lst n)
    (cond ((< n 0) nil)
          ((= n 0) (cons () lst))
          ((null? lst) (list lst-so-far))
          ((= n 1) (cons (append lst-so-far (list (car lst))) (cdr lst)))
          (else (helper (append lst-so-far (list (car lst))) (cdr lst) (- n 1)))))
  (helper nil lst n)
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
  (lambda (x) (if (null? funcs) x ((compose-all (cdr funcs)) ((car funcs) x))))
)

