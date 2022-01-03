;nyquist plug-in
;version 4
;type tool
;name "Clip label"
;author "Paul Tran"
;release 2.3.1
;copyright "Released under terms of the GNU General Public License version 2"

(setf trim-buffer 0.3)

(defun select (start end)
  (aud-do (format nil "Select:Start=~a End=~a Mode=Set" start end)))


(defun get-last-region (labels)
  (let ((last-label (nth (1- (length labels)) labels)))
;    (print last-label)
    (list (- (first last-label) trim-buffer)
           (+ (second last-label) trim-buffer))))

(setf labels (second (first (aud-get-info "Labels"))))
(setf region (get-last-region labels))
(select (first region) (second region))